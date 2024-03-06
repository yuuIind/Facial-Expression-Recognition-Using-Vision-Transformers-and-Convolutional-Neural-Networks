import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"MCCT-1_merged.csv")
# Assuming df is your DataFrame
# Plot Loss
plt.plot(df['Epoch'], df['Loss'], label='Training Loss')
plt.plot(df['Epoch'], df['VAL_Loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Value')
plt.title('MCCT-1 Without Oversampling Training & Validation Loss')
plt.legend()
plt.grid()
plt.savefig('loss.png')
plt.show()

# Plot Accuracy
plt.plot(df['Epoch'], df['Accuracy'], label='Training Accuracy')
plt.plot(df['Epoch'], df['VAL_Accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Value')
plt.title('MCCT-1 Without Oversampling Training & Validation Accuracy')
plt.legend()
plt.grid()
plt.savefig('accuracy.png')
plt.show()