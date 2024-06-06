# CellphoneRS
Cellphone Recommendation System using Machine Learning | Collaborative Filtering Based

**Dataset: [Amazon Cell Phones Reviews](https://www.kaggle.com/datasets/grikomsn/amazon-cell-phones-reviews)**

## How to build
1. Clone this repo
2. Create `data` and `artifacts` folders. Download the **dataset** and put it in the `data` folder
    ```
    mkdir data
    mkdir artifacts
    ```
3. Create virtual environment
    ```
    py -m venv venv
    ```
4. Activate virtual environment
    ```
    venv\Scripts\activate.bat
    ```
5. Install the library
    ```
    pip install -r requirements.txt
    ```
6. Execute **jupyter notebook** to build **model**
7. Run app
    ```
    streamlit run app.py
    ```
