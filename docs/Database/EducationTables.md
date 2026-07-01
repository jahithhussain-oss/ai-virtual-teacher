### Table Definitions boards

board_id

name

country

language

status

created_at

### Table Definitions academic_years

year_id

board_id

year

version

status

### Table Definitions grades

grade_id

board_id

year_id

name

display_order

### Table Definitions subjects

subject_id

grade_id

name

code

language

### Table Definitions subjects

subject_id

grade_id

name

code

language

### Table Definitions chapters

chapter_id

subject_id

number

title

summary

estimated_hours

### Table Definitions topics

topic_id

chapter_id

title

difficulty

learning_time

### Table Definitions sub_topics

sub_topic_id

topic_id

title

description

### Table Definitions concepts

concept_id

sub_topic_id

title

definition

importance

### Table Definitions learning_objects

learning_object_id

concept_id

type

title

content

language

difficulty

version

