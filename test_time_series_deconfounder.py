
# from simulated_autoregressive import AutoregressiveSimulation
# autoregressive = AutoregressiveSimulation(args.gamma, args.num_simulated_hidden_confounders)
# dataset = autoregressive.generate_dataset(5000, 31)
#
# print(dataset)

python main_time_series_deconfounder.py --gamma=0.6 --exp_name='trying' \
--num_simulated_hidden_confounders=1 --num_simulated_hidden_confounders=1  --results_dir='results2'
