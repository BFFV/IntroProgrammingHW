import glob
import subprocess
import filecmp
import os
import sys
import platform

CODE = sys.argv[1:]

SO = platform.system()
_path = 'files/w'if SO=='Windows' else 'files/u'
TEMP = '{}/temp.txt'.format(_path)
PATHS = ['{}/p1'.format(_path), '{}/p2'.format(_path), '{}/p3'.format(_path)]
RESPONSES = ['ACCEPTED', 'RUNTIME_ERROR', 'WRONG_ANSWER', 'TIMEOUT']

if SO=='Windows':
    os.environ["COMSPEC"] = r"C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe"

def get_program_name(program):
    return program.split('/')[-1][:-3]

def run_for_console_output(program, inp, outp):

    _python = '' if SO=='Windows' else '3'
    _cat = 'Get-Content' if SO=='Windows' else 'cat'

    outfile = open(TEMP, 'w+')
    cmd = '{} {} | python{} {}'.format(_cat, inp, _python, program)

    try:
        result = subprocess.call(cmd, shell = True ,stdout=outfile, stderr=outfile, timeout = 1)
    except subprocess.TimeoutExpired:
        return 3
    except:
        return 1
    finally:
        outfile.close()
    if result:
        return 1

    return 0 if filecmp.cmp(TEMP, outp) else 2

def run_for_file_output(program, inp, expected_outp, program_outp):
    try:
        os.remove(program_outp)
    except:
        pass
    
    _python = '' if SO=='Windows' else '3'
    _cat = 'Get-Content' if SO=='Windows' else 'cat'

    outfile = open(TEMP, 'w+')
    cmd = '{} {} | python{} {}'.format(_cat, inp, _python, program)

    try:
        result = subprocess.call(cmd, shell = True, stdout=outfile, stderr=outfile, timeout = 1)
    except subprocess.TimeoutExpired:
        return 3
    except:
        return 1
    finally:
        outfile.close()
    if result:
        return 1
    return 0 if filecmp.cmp(expected_outp, program_outp) else 2


def run_p1():
    title = 'Programa;test1;test2;test3;test4;total'
    p = CODE[0]
    result = get_program_name(p)
    total = 0
    for i in range(1,5):
        inp = '{}/testcases/input0{}.txt'.format(PATHS[0], i)
        outp = '{}/testcases/output0{}.txt'.format(PATHS[0], i)
        resp = run_for_console_output(p, inp, outp)
        total += resp
        print('Test{}: {}'.format(i,RESPONSES[resp]))
    print('WRONG' if total else 'SOLVED')

def run_p2():
    title = 'Programa;test1;test2;total'
    p = CODE[1]
    result = get_program_name(p)
    total = 0
    for i in range(1,3):
        inp = '{}/testcases/input0{}.txt'.format(PATHS[1], i)
        expected_outp = '{}/testcases/file0{}_filtrado_result.csv'.format(PATHS[1], i)
        program_outp = '{}/testcases/file0{}_filtrado.csv'.format(PATHS[1], i)
        resp = run_for_file_output(p, inp, expected_outp, program_outp)
        total += resp
        print('Test{}: {}'.format(i,RESPONSES[resp]))
    print('WRONG' if total else 'SOLVED')

def run_p3():
    title = 'Programa;test1;test2;total'
    p = CODE[2]
    result = get_program_name(p)
    total = 0
    for i in range(1,3):
        inp = '{}/testcases/input0{}.txt'.format(PATHS[2], i)
        expected_outp = '{}/testcases/file0{}_final_result.txt'.format(PATHS[2], i)
        program_outp = '{}/testcases/file0{}_final.txt'.format(PATHS[2], i)
        resp = run_for_file_output(p, inp, expected_outp, program_outp)
        total += resp
        print('Test{}: {}'.format(i,RESPONSES[resp]))
    print('WRONG' if total else 'SOLVED')


if __name__ == '__main__':
    run_p1()
    run_p2()
    run_p3()
