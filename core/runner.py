from .settings import *
from submission.models import Round, Run
import shutil
import judger


def controller(round_id):
    def copy_files():
        problem_path = os.path.join(PROBLEM_PATH, str(problem.id))
        shutil.copytree(problem_path, path)
        for submission in submission_list:
            src_path = os.path.join(COMPILE_PATH, str(submission.id), settings[submission]['exe_name'])
            dst_path = os.path.join(path, str(submission.id))
            shutil.copyfile(src_path, dst_path)
            os.chmod(dst_path, 0o777)

    def runner(submission, max_cpu_time, max_memory):
        exe_cmd = settings[submission]['execute_command']
        if submission.language == 'j':
            max_memory = UNLIMITED
            exe_cmd = exe_cmd.format(exe_path=path,
                                     exe_name=str(submission.id),
                                     max_memory=max_memory * 3
                                     ).split()
        else:
            exe_cmd = exe_cmd.format(exe_path=path,
                                     exe_name=str(submission.id)
                                     ).split()
        in_file = os.path.join(path, 'in')
        out_file = os.path.join(path, 'out')
        log_file = os.path.join(path, 'log')
        _run_result = judger.run(path=exe_cmd[0],
                                 max_cpu_time=max_cpu_time,
                                 max_memory=max_memory,
                                 in_file=in_file,
                                 out_file=out_file,
                                 args=exe_cmd[1:],
                                 env=["PATH=" + os.environ["PATH"]],
                                 log_path=log_file,
                                 # use_sandbox=settings[submission]['use_sandbox'],
                                 use_sandbox=False,
                                 use_nobody=False,
                                 )
        if submission.language == 'j' and run_result['memory'] > max_memory*1.5:
            _run_result['flag'] = 3
        print(_run_result)
        return _run_result

    def judge():
        exe_cmd = JUDGE_EXE_CMD.format(exe_path=path, exe_name=JUDGE_NAME).split()
        _run_result = judger.run(path=exe_cmd[0],
                                 max_cpu_time=UNLIMITED,
                                 max_memory=UNLIMITED,
                                 in_file=os.path.join(path, "hehe"),
                                 out_file=_judge_result_path,
                                 args=exe_cmd[1:],
                                 env=["PATH=" + os.environ["PATH"]],
                                 use_sandbox=False,
                                 use_nobody=False,
                                 )
        print(_run_result)

    path = os.path.join(RUN_PATH, str(round_id))
    current_round = Round.objects.get(pk=round_id)
    submission_list = list(current_round.submissions.all())
    problem = submission_list[0].problem
    _time_limit = problem.time_limit
    _memory_limit = problem.memory_limit * 1048576

    _judge_result_path = os.path.join(path, JUDGE_RESULT_NAME)

    settings = {submission: LANGUAGE_SETTINGS[submission.language] for submission in submission_list}
    copy_files()
    os.chdir(path)

    while True:
        for submission in submission_list:
            current_run = Run()
            current_run.round = current_round

            run_result = runner(submission, max_cpu_time=_time_limit, max_memory=_memory_limit)
            current_run.running_time = run_result['cpu_time']
            current_run.running_memory = run_result['memory']

            # print(run_result)
            if run_result['flag']:
                current_run.save()
                return
            judge()
            with open(_judge_result_path) as f:
                next_step, judge_result_message = f.read().split('\n')[:2]
            current_run.result = ERROR_FLAG[run_result['flag']]
            current_run.message = judge_result_message
            current_run.save()
            print(next_step, judge_result_message)
            if next_step == 'stop':
                return









