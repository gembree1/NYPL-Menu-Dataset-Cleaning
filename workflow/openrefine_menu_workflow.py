# @BEGIN OpenRefine_Menu

# @IN name @URI file:Menu.csv
# @IN sponsor @URI file:Menu.csv
# @IN event @URI file:Menu.csv
# @IN venue @URI file:Menu.csv
# @IN place @URI file:Menu.csv
# @IN physical_description @URI file:Menu.csv
# @IN occasion @URI file:Menu.csv
# @IN notes @URI file:Menu.csv
# @IN date @URI file:Menu.csv
# @IN location @URI file:Menu.csv
# @IN pass_thru_cols @URI file:Menu.csv
# @OUT Menu.csv.tsv @URI file:Dish.csv.tsv

# @BEGIN remove_special_characters
# @IN name
# @OUT name_t1
# @END remove_special_characters
# @BEGIN cluster_keycollison_fingerprint
# @IN name_t1
# @OUT name_t2
# @END cluster_keycollison_fingerprint

# @BEGIN remove_special_characters
# @IN sponsor
# @OUT sponsor_t1
# @END remove_special_characters
# @BEGIN cluster_keycollison_fingerprint
# @IN sponsor_t1
# @OUT sponsor_t2
# @END cluster_keycollison_fingerprint

# @BEGIN remove_special_characters
# @IN event
# @OUT event_t1
# @END remove_special_characters
# @BEGIN cluster_keycollison_fingerprint
# @IN event_t1
# @OUT event_t2
# @END cluster_keycollison_fingerprint

# @BEGIN remove_special_characters
# @IN venue
# @OUT venue_t1
# @END remove_special_characters
# @BEGIN cluster_keycollison_fingerprint
# @IN venue_t1
# @OUT venue_t2
# @END cluster_keycollison_fingerprint

# @BEGIN remove_special_characters
# @IN place
# @OUT place_t1
# @END remove_special_characters
# @BEGIN cluster_keycollison_fingerprint
# @IN place_t1
# @OUT place_t2
# @END cluster_keycollison_fingerprint

# @BEGIN copy_and_extract_dimension
# @IN physical_description
# @OUT dimension
# @END copy_and_extract_dimension

# @BEGIN remove_dimension
# @IN physical_description
# @OUT physical_description_t1
# @END remove_dimension

# @BEGIN cluster_keycollison_fingerprint
# @IN physical_description_t1
# @OUT physical_description_t2
# @END cluster_keycollison_fingerprint

# @BEGIN remove_special_characters
# @IN occasion
# @OUT occasion_t1
# @END remove_special_characters
# @BEGIN cluster_keycollison_fingerprint
# @IN occasion_t1
# @OUT occasion_t2
# @END cluster_keycollison_fingerprint

# @BEGIN cluster_keycollison_fingerprint
# @IN notes
# @OUT notes_t1
# @END cluster_keycollison_fingerprint

# @BEGIN filter_outside_year_range_1851_2012
# @IN date
# @OUT date_t1
# @END filter_outside_year_range_1851_2012

# @BEGIN cluster_keycollison_fingerprint
# @IN location
# @OUT location_t1
# @END cluster_keycollison_fingerprint

# @BEGIN export
# @IN name_t2
# @IN sponsor_t2
# @IN event_t2
# @IN venue_t2
# @IN place_t2
# @IN physical_description_t2
# @IN occasion_t2
# @IN notes_t1
# @IN date_t1
# @IN location_t1
# @IN dimension
# @IN pass_thru_cols
# @OUT Menu.csv.tsv @URI file:Dish.csv.tsv
# @END export

# @END OpenRefine_Menu
