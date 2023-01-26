import datetime
import re
import os
import numpy as np

class helper:
    info = """
    author: S.Jaidheer
    github: JAIDHEER007

    Path finding using Python

    INFO
    ==============================================================
    Date: {fdate}
    time: {ftime}

    Rows: {frows}
    Cols: {fcols}
    ==============================================================

    """

    def createFolder(cwd, initialState, extraInfo = {}, directories = []) -> str:
        # Getting Current Time
        curr = datetime.datetime.now()
        dateStr = str(curr.date())
        timeStr = str(curr.time())

        # Folder Name
        directory = "Run_" + re.sub('\D', '', dateStr) + "_" + re.sub('\D', '', timeStr)

        # Final Path
        fPath = os.path.join(cwd, 'TestRuns', directory)

        # Creating a Directory
        os.mkdir(fPath)

        # Making the extra Directories if Needed
        for directory in directories:
            dirPath = os.path.join(fPath, directory)
            os.mkdir(dirPath)

        # Writing the useful files

        # Saving the initial grid state
        np.savetxt(fname = os.path.join(fPath, 'initialState.csv'), 
                   X = initialState, delimiter = ',', fmt='%d')

        rows, cols = initialState.shape
        with open(os.path.join(fPath, 'info.txt'), 'w') as fileHandle:
            fileHandle.write(helper.info.format(fdate = dateStr, 
                                                ftime = timeStr, 
                                                frows = rows, 
                                                fcols = cols))

            for name, info in extraInfo.items():
                fileHandle.write("{fname}: {finfo}".format(fname = name, finfo = info))

        return fPath 