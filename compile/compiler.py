from .celery import app
from .language_settings import lang_settings
from AIPlayground.settings import BASE_DIR
import os
from submission.models import Submission
import judger


@app.task
def compiler(submission_id):
    submission = Submission.objects.get(pk=submission_id)
    language = submission.language
    code = submission.code

    lang_setting = lang_settings[language]

    judge_base_path = os.path.join(BASE_DIR, "workspace", str(submission_id))
    os.mkdir(judge_base_path)
    src_path = os.path.join(judge_base_path, lang_setting['src_name'])
    with open(src_path, "w") as f:
        f.write(code)

    compile_command = lang_setting['compile_command'].format(src_path=src_path, exe_path=judge_base_path).split(" ")
    compiler_output_file = os.path.join(judge_base_path, "compiler.out")
    compile_result = judger.run(path=compile_command[0],
                                in_file="/dev/null",
                                out_file=compiler_output_file,
                                max_cpu_time=lang_setting["compile_max_cpu_time"],
                                max_memory=lang_setting["compile_max_memory"],
                                args=compile_command[1:],
                                env=["PATH=" + os.environ["PATH"]],
                                use_sandbox=False,
                                use_nobody=False)  # not using nobody

    with open(compiler_output_file) as compile_output_handler:
        compile_output = compile_output_handler.read().strip()
    if compile_result['flag'] != 0:
        submission.verdict = '130'
        if compile_output:
            submission.compile_error = compile_output
        else:
            submission.compile_error = "Compile error, info: " + str(compile_result)
    else:
        submission.verdict = '131'
        with open(os.path.join(judge_base_path, lang_setting['exe_name']), "rb") as f:
            submission.compile_result.save(lang_setting['exe_name'], f)
    submission.save()