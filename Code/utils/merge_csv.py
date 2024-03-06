import pandas as pd

def merge_csv(csv_list, output_path):
    for i in range(len(csv_list)):
        if i == 0:
            df = pd.read_csv(csv_list[i])
        else:
            df = pd.concat([df, pd.read_csv(csv_list[i])], ignore_index=True)
    
    df.to_csv(output_path, index=False)

if __name__ == '__main__':
    csv_list = [r'VCCT-2_loss_log_3.csv',
                r'VCCT-2_loss_log_7.csv',
                r'VCCT-2_OS_loss_log_10.csv',]
    output_path = 'VCCT-2_OS_merged.csv'
    merge_csv(csv_list, output_path)
