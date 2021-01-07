import os
import sys

subCMakeListsContent = '''
FILE(GLOB_RECURSE INCLUDE_FILES
    ${PROJECT_SOURCE_DIR}/*.h
    ${PROJECT_SOURCE_DIR}/*.hpp
)

FILE(GLOB_RECURSE SRC_FILES 
    ${PROJECT_SOURCE_DIR}/*.c
    ${PROJECT_SOURCE_DIR}/*.cpp
)

SOURCE_GROUP("Header Files"            FILES "${INCLUDE_FILES}")
SOURCE_GROUP("Source Files"            FILES "${SRC_FILES}")

ADD_EXECUTABLE(
    ${PROJECT_NAME}
    ${INCLUDE_FILES}
    ${SRC_FILES}
)
SET_TARGET_PROPERTIES(${PROJECT_NAME} PROPERTIES LINK_FLAGS "/SUBSYSTEM:WINDOWS")
TARGET_LINK_LIBRARIES(${PROJECT_NAME} include ddraw)
'''

if __name__ == "__main__":
    for n in range(1, 19):
        chaptDirName = "Chapt_" + str(n).zfill(2)
        for root, dirs, files in os.walk(chaptDirName):
            foutPath = os.path.join(root, "CMakeLists.txt")
            fout = open(foutPath, "w")
            for oneDir in dirs:
                subFourPath = os.path.join(root, oneDir, "CMakeLists.txt")
                subFout = open(subFourPath, "w")
                subFout.writelines([
                    "PROJECT({})".format(oneDir), subCMakeListsContent,
                    "SET_TARGET_PROPERTIES({0} PROPERTIES FOLDER \"{1}\")".format(oneDir, root)
                ])
                subFout.close()
                print("{} finished.".format(subFourPath))
                fout.write("ADD_SUBDIRECTORY({})\n".format(oneDir))
            fout.close()
            print("{} finished.".format(foutPath))
            break
