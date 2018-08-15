from zipfile import ZipFile as zp
import argparse as ap
import os
import random

class zippy:
    def CreateZipFile(self,name=None,path=None):
        """name name of the zip file you want to create\n
            path is the path of the directory you want ton archived
        """
        if name is None:
            name=self.RandomName()
        if path is None:
            path=os.getcwd()
        assert os.path.isdir(path),"You need to pass in a directory"
        
        dirfile=os.listdir(path)
        with zp(name,"a") as zippyfile:
            for file in dirfile:
                zippyfile.write(file)

    def ExtractSpecificFile(self,name,zip):
        """name is the name of the file you want to extract from the zip\n
            zip is the archive file you want to extarct from
        """
        with zp(zip) as myzip:
            with myzip.open(name) as myfile:
                with open(name,"a") as savefile:
                    savefile.write(myfile.read())

    def ExtractAllFileInADir(self,path,pathtoextractto=None):
        if pathtoextractto==None:
            pathtoextractto=os.getcwd()
        with zp(path) as zippyextract:
            zippyextract.extractall(path=path)
            
    def RandomName(self):
        alPhabeths="abcdefghijklmnopqrstuvwxyz"
        alPhabeths+="".join([i.swapcase() for i in alPhabeths])
        alPhabeths+="1234567890"
        randomName="zippy_"
        lenAlphabeths=len(alPhabeths)
        for _ in range(5):
            randomName+=alPhabeths[random.randint(0,lenAlphabeths)]
        randomName+=".zip"
        return randomName
    def HasExtension(self,filename):
        ext=filename.split(".")[-1]
        return len(ext)==3 and ext!='zip'

parser = ap.ArgumentParser()
parser.add_argument("--operation", type=str, default="", help="choose operation to perform E"+
                    " to extract file ,e to extract specific file,C")
parser.add_argument("--path", type=str, default=os.getcwd(), help="path to the zip file or extracted file")
parser.add_argument("--name", type=str, default=None, help="name of the extracted file")
args = parser.parse_args()

z=zippy()
if args.operation=="E":
    z.ExtractAllFileInADir(path=args.path)
elif args.operation=="e":
    z.ExtractSpecificFile(args.name,args.path)
else:
    z.CreateZipFile(name=args.name,path=args.path)
