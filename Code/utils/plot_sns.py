import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set seaborn style
sns.set()

# Load data
df = pd.read_csv(r"C:\Users\hakan\Downloads\MCCT-2_OS_loss_log_10.csv")

# Plot Loss
plt.figure(figsize=(12, 6))
plt.plot(df['Epoch'], df['Loss'], label='Training Loss', color='tab:blue', lw=2)
plt.plot(df['Epoch'], df['VAL_Loss'], label='Validation Loss', color='tab:orange', lw=2, linestyle='--')
plt.xlabel('Epoch', fontsize=14)
plt.ylabel('Loss Value', fontsize=14)
plt.title('VCCT-2 With Oversampling Training & Validation Loss', fontsize=20, weight='bold', pad=20)
plt.legend(loc='best', fontsize=14, frameon=False)
plt.grid(linestyle='--', linewidth=0.5)
plt.savefig('loss.png', dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()

# Plot Accuracy
plt.figure(figsize=(12, 6))
plt.plot(df['Epoch'], df['Accuracy'], label='Training Accuracy', color='tab:green', lw=2)
plt.plot(df['Epoch'], df['VAL_Accuracy'], label='Validation Accuracy', color='tab:red', lw=2, linestyle='--')
plt.xlabel('Epoch', fontsize=14)
plt.ylabel('Accuracy Value', fontsize=14)
plt.title('VCCT-2 With Oversampling Training & Validation Accuracy', fontsize=20, weight='bold', pad=20)
plt.legend(loc='best', fontsize=14, frameon=False)
plt.grid(linestyle='--', linewidth=0.5)
plt.savefig('accuracy.png', dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()