import YoshiViz.report_generator
import os

if __name__ == '__main__':
    YoshiViz.report_generator.\
        generate_pdf_report(os.path.join(os.path.abspath('.'),
                                         'YoshiViz', 'input.txt'), 'SignalR')

