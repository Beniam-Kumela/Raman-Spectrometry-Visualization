#import python modules
import pandas as pd
import matplotlib.pyplot as plt

iter_var = True
while iter_var:
    
    try:
        
        #read and create dataframe of the excel file
        inp = input('Enter file name (type "exit" if no more file names): ')
        if inp == 'exit':
            iter_var = False
        filename = inp + '.xlsx'
        df = pd.read_excel(filename, sheet_name = 'Sheet1', header = None)
        try:

            # data cleaning and acquisition
            x_axis = df.iloc[:, 0]
            for i in range(df.shape[1]):
                y_axis = df.iloc[:, i]
                plt.plot(x_axis, y_axis)
                plt.xlabel('Raman shift / cm -1')
                plt.ylabel('Counts')

            # present the overlayered line plot graph in pyplot viewer
            plt.title('Raman shift / cm -1 vs Counts')
            print('Make sure to save the displayed graph.')
            plt.show()

        except:
            print('Error in graph formation, revise program!')

    except:
        print('Error in reading file! Make sure this script is placed within the data folder.')
    

        