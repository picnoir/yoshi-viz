from YoshiViz import  report_generator
import os

if __name__ == '__main__':
    report_generator.\
        generate_pdf_report(os.path.join(os.path.abspath('.'),
                                         'YoshiViz', 'input.txt'), 'SignalR', 'Community Type')

