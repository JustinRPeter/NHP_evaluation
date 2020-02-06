
# Author: Elisabeth Vogel, elisabeth.vogel@bom.gov.au
# Date: 26/03/2019

# load required netcdf modules
module load netcdf cdo nco


# read in variable
var=$1
path_climate_data=$2
out_path=$3

mkdir -p ${out_path}

# prepare file names
files=`find ${path_climate_data} -type f -name "*${var}*19600101-20051231.nc4" -exec basename {} \;`

for file in ${files}; do
    echo ${file}
    cdo -O -z zip9 splityear ${path_climate_data}/${file} ${out_path}/${file%.nc4}_
done
    
    
