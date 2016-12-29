from .celery import app
from .settings import *
from core.runner import controller
from submission.models import Submission, Round
import judger
import os


@app.task
def compiler(submission_id):
    submission = Submission.objects.get(pk=submission_id)
    setting = LANGUAGE_SETTINGS[submission.language]
    code = submission.code

    path = os.path.join(COMPILE_PATH, str(submission_id))
    os.mkdir(path)
    src_path = os.path.join(path, setting['src_name'])
    with open(src_path, "w") as f:
        f.write(code)

    compile_command = setting['compile_command'].format(src_path=src_path, exe_path=path).split(" ")
    compiler_output_file = os.path.join(path, "compiler.out")
    submission.verdict = 129
    submission.save()
    compile_result = judger.run(path=compile_command[0],
                                in_file="/dev/null",
                                out_file=compiler_output_file,
                                max_cpu_time=setting["compile_max_cpu_time"],
                                max_memory=setting["compile_max_memory"],
                                args=compile_command[1:],
                                env=["PATH=" + os.environ["PATH"]],
                                use_sandbox=False,
                                use_nobody=False)  # not using nobody
    print("Compile: " + str(compile_result))

    with open(compiler_output_file) as compile_output_handler:
        compile_output = compile_output_handler.read().strip()
    if compile_result['flag'] != 0:
        submission.verdict = 130
        if compile_output:
            submission.compile_error = compile_output
        else:
            submission.compile_error = "Compile error, info: " + str(compile_result)
    else:
        submission.verdict = 131
    submission.save()

    # Starting round
    if submission.verdict == 131:
        sublist = list(Submission.objects.filter(problem=submission.problem, verdict=131))
        for opponent in sublist:
            round = Round()
            round.save()
            round.submissions.add(opponent, submission)
            round.save()
            controller(round.id)
