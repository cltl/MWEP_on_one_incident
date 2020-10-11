

json_dir='../dev'
lib_dir='../lib'
log_dir='../output/log';

mkdir -p $log_dir;

verbose=5;

cd $lib_dir;

for json in $json_dir/*json;
  do
    basename="$(basename -- $json .json)"

    echo;
    echo $basename;
    echo $(date);
    python crawl_ref_texts_of_one_event_instance.py --config_path=$json --verbose=$verbose > $log_dir/$basename.out 2> $log_dir/$basename.err &
    echo $(date);
done