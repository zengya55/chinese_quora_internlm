import os
os.system('python download_hf.py')
os.system('streamlit run app.py --server.address=0.0.0.0 --server.port 7860')