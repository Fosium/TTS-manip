import subprocess
import os

def main(INPUTDIR, OUTPUTDIR):
    for f in os.listdir(INPUTDIR):
        print(f'Now working on file {f}')
        outname = f.split(".")[0]
        inpath = INPUTDIR+"\\"+f
        outpath = OUTPUTDIR + "\\" + outname
        command = f'type "{inpath}" | .\piper.exe -m .\en_US-ryan-high.onnx -f {outpath}.wav'
        print(f"Running command {command}")
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(f"Output of '{command}':\n{result.stdout}")
        if result.stderr:
            print(f"Error output of '{command}':\n{result.stderr}")

main("INPUTPATH", "OUTPUTPATH")
