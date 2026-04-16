from src.train import train
from src.predict import predict

if __name__ == "__main__":
    train()
    
    sample = [5.1,3.5,1.4,0.2]
    result = predict(sample)
    
    print("Prediction:",result)

# install manually  
# pip install scikit-learn pandas joblib pytest


# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/PranavSankpal2003/CICD_IRIES.git
# git push -u origin main