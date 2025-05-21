import argparse
import sys

from collectmeteranalog import glob
from collectmeteranalog.collect import collect
from collectmeteranalog.labeling import label
from collectmeteranalog.predict import load_interpreter



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--collect', help='Collect images from AI-on-the-Edge-Device. Define name or IP address (e.g. http://IP-ADDRESS)')
    parser.add_argument('--days', type=int, default=3, help='Define in days how many images shall be collected. (default: 3)')
    parser.add_argument('--keepdownloads', action='store_true', help='Normally all collected images will be deleted. If defined the images are kept.')
    parser.add_argument('--nodownload', action='store_true', help='Do not collect any images. Only remove duplicates and labeling.')
    parser.add_argument('--startlabel', type=float, default=0.0, help='Process only images >= startlabel. (default: 0.0 --> all)')
    parser.add_argument('--saveduplicates', action='store_true', help='Save the duplicates in an intermediate subdirectory in raw_images.')
    parser.add_argument('--ticksteps',type=int, default=1, help='How many label ticks are shown (1 = 0.1 steps, 2 = 0.2 steps, ... | max = 5)')
    parser.add_argument('--similiarbits', type=int, default=2, help='How many pixels must be different if an image is not similiar to others')
    parser.add_argument('--labeling', default=None, help='Path to image folder containing images which shall be labeled.')
    parser.add_argument('--labelfile', default=None, help='Path to a CSV file containing an indexed list of images which shall be labeled.')
    parser.add_argument('--model', default='off', help='Path to model file if an external model should be used (default: off --> No model)')
    parser.add_argument('--version', action='store_true', help='Show application version')


    # print help message if no argument is given
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    args = parser.parse_args()

    if args.version:
        from collectmeteranalog.__version__ import __version__
        print(f"{__version__}")
        sys.exit(0)

    if (args.ticksteps < 1 or args.ticksteps > 5):
        args.ticksteps = 1

    if (args.collect != None):
        collect(args.collect, args.days, keepolddata=args.keepdownloads, download=not args.nodownload,
                    startlabel=args.startlabel, ticksteps=args.ticksteps, similarbits=args.similiarbits,
                    saveduplicates=args.saveduplicates)
    elif (args.labeling != None):
        if (args.model != None):
            glob.model_path = args.model
            load_interpreter(args.model)

        if (args.labelfile != None):
            label(args.labeling, args.startlabel, args.labelfile, ticksteps=args.ticksteps)    
        else:
            label(args.labeling, args.startlabel, ticksteps=args.ticksteps)   
    else:
        print("Error: You must specify either --collect or --labeling")
        parser.print_help(sys.stderr)
        sys.exit(1) 

if __name__ == '__main__':
    main()