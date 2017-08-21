# @BEGIN OpenRefine_Dish

# @IN name @URI file:Dish.csv
# @IN pass_thru_cols @URI file:Dish.csv
# @OUT Dish.csv.tsv @URI file:Dish.csv.tsv

# @BEGIN value.trim() 
# @IN name
# @OUT name_t1
# @end value.trim() 

# @BEGIN value.replace(/\s+/,'')
# @IN name_t1
# @OUT name_t2
# @end value.replace(/\s+/,'')

# @BEGIN value.toLowercase()
# @IN name_t2
# @OUT name_t3
# @end value.toLowercase()

# @BEGIN value.replace(value, /[%@#!\\\[\](),.&"':;\-_\*<>]/, '')
# @IN name_t3
# @OUT name_t4
# @end value.replace(value, /[%@#!\\\[\](),.&"':;\-_\*<>]/, '')

# @BEGIN cluster_keycollison_fingerprint
# @IN name_t4
# @OUT name_t5
# @end cluster_keycollison_fingerprint

# @BEGIN export
# @IN name_t5
# @IN pass_thru_cols 
# @OUT Dish.csv.tsv @URI file:Dish.csv.tsv
# @end export

# @END OpenRefine_Dish
