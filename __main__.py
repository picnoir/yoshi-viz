from YoshiViz import report_generator, decision_tree_algorithm
import os


if __name__ == '__main__':
    #file director
    fileDirectory = os.path.join(os.path.abspath('.'), 'YoshiViz', 'input.txt')
    #test decision tree
    repositoryName = input("Please input repository name:\n")
    tempCommunityType = decision_tree_algorithm.\
        community_type(fileDirectory,repositoryName)
    """
    report_generator.\
            generate_pdf_report(fileDirectory, repositoryName, tempCommunityType)
    """
    print('the type of', repositoryName, 'is', tempCommunityType, '\n"check .\YoshiViz\output"')
