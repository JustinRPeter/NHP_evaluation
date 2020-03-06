import os
# turn off all warnings
import warnings; warnings.simplefilter('ignore')


### Functions

# import data evaluation plotting functions
import evaluation as evl


### Parameters
parameters = evl.config.load_config()

# prepare settings
skip_existing = parameters['skip_existing']
data_path_ref = parameters['data_path_processed_ref']
data_path_sim = parameters['data_path_processed_sim']
plot_path = os.path.join(parameters['plot_path'], '03_timeseries')
year_start = parameters['evaluation_year_start']
year_end = parameters['evaluation_year_end']
name_sim_prefix = parameters['name_sim_prefix']
name_ref = parameters['name_ref']
gcms = parameters['gcms']
vars = parameters['vars']
ref_vars = parameters['ref_vars']
ref_vars_in_nc = parameters['ref_vars_in_nc']
sim_vars = parameters['sim_vars']
sim_vars_in_nc = parameters['sim_vars_in_nc']

statistics = parameters['timeseries_statistics']

# read in mask
mask = parameters['mask_file']


#### Plot all time series

# Reading and preparing data
for var in vars:
            
    print(var)
    var_sim = sim_vars[var]
    var_sim_in_nc = sim_vars_in_nc[var]
    var_ref = ref_vars[var]
    var_ref_in_nc = ref_vars_in_nc[var]

    df = None

    fn_plot = os.path.join(plot_path, 'timeseries_%s_%s_%s.png' % (var, year_start, year_end))
    print('Preparing plot: %s' % fn_plot)

    if not os.path.exists(fn_plot) or not skip_existing:
        
        # read in data
        print('Reading in data')
        df = evl.read_in.prepare_timeseries_for_all_gcms_and_statistics(
            data_path_ref=data_path_ref, data_path_sim=data_path_sim,
            gcms=gcms, var=var, name_sim_prefix=name_sim_prefix,
            name_ref=name_ref, statistics=statistics, year_start=year_start, year_end=year_end,
            mask=mask, var_ref=var_ref, var_sim=var_sim, var_ref_in_nc=var_ref_in_nc, var_sim_in_nc=var_sim_in_nc)
        
        # plot data
        evl.plotting.plot_timeseries(dataframe=df, x='year', y=var, var=var, name_sim_prefix=name_sim_prefix,
                        name_ref=name_ref, fn_plot=fn_plot)

