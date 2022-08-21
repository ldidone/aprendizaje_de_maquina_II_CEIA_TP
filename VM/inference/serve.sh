activate () {
  . ../venv/bin/activate
}

echo Activating virtualenv
activate

echo Serving model
mlflow models serve -m /home/lucas_crar14/acoustic_extinguisher_fire/train/mlruns/0/49c8ab441b75423a88c4c71c05f3e740/artifacts/decision_tree_model --no-conda -h 0.0.0.0
