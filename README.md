# Student Grade Dashboard
A dashboard for visualizing student grades data from csv files

## Scope
Creating an interactive and exploarotary dashboard to understand the given data better
## How to run:
*Note that you will need the following installed on your machine:*
   - git
   - python (>= 3.12)

First clone the repository

```bash
git clone https://github.com/Goaten-31/PyProj.git
```
or if you're using an ssh key
```bash
git clone git@github.com:Goaten-31/PyProj.git
```

After you've successfully cloned the repo, activate a virtual environment (venv):
1. Create a venv
```bash
python -m venv .venv #note that ".venv" can be named however you like
```
2. Activate the venv
    - On Unix Based Systems:
    ```bash
    sudo source .venv/bin/activate
   ```
   - On Windows:
    ```shell
    Set-executionPolicy -Scope Process -ExecutionPolicy RemoteSigned
    .venv/Scripts/activate
    ```

Once your venv is active, install the necessary dependencies
```bash
pip install -r requirements.txt
```

After executing these steps successfully, you can now run your app with:
```bash
streamlit run app.py
```