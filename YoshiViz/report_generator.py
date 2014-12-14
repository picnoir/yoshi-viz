import os
import json
from jinja2 import Template


def generate_pdf_report(yoshi_output_file, project_name, community_type):
    """
    Generates a PDF report of a given output of Yoshi.
    :param yoshi_output_file: Path to the Yoshi output file.
    :param project_name: Name of the project.
    :param community_type
    """
    yoshi_file = open(yoshi_output_file, "r")
    json_data = json.load(yoshi_file)
    community_index = _find_community_index(json_data, project_name)
    yoshi_file.close()
    template_file = open(os.path.join(os.path.abspath('.'),
                                      'YoshiViz', 'output', 'template.jinja'), 'r')
    template = Template(template_file.read())
    template_file.close()
    output = template.render(DataQuality=json_data['DataQuality'][community_index],
                             DataCommunity=json_data['DataCommunity'][community_index],
                             community_type=community_type)
    output_file = open(os.path.join(os.path.abspath('.'), 'YoshiViz', 'output',
                                    project_name + '_report.html'), 'w')
    output_file.write(output)
    output_file.close()


def _find_community_index(json_data, community_name):
    """
    DANGER

    Extracts the various community metrics from a json string.
    :param json_data: json string.
    :param community_name: Name of the community to extract.
    :return: Community object of the wanted community.
    """

    #First we retrieve the good community from the mess up json…
    index = 0
    found = False
    while not found:
        try:
            if json_data['DataQuality'][index]['RepoName'] == community_name:
                return index
            else:
                index += 1
        except:
            raise Exception("The community " +
                            community_name + " cannot be found in the specified file.")

