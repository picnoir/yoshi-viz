from YoshiViz import    report_generator
from YoshiViz import    decision_tree_algorithm
import os


#file director        
fileDirectory = '.\YoshiViz\input.txt'
#test decision tree
repositoryName = input("Please input repository name:\n")
tempCommunityType = decision_tree_algorithm.\
      CommunityType(fileDirectory,repositoryName)
if __name__ == '__main__':
    report_generator.\
        generate_pdf_report(fileDirectory, repositoryName, tempCommunityType)
    print('the type of', repositoryName,'is', tempCommunityType , '\n"check .\YoshiViz\output"')
