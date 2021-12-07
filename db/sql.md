```sql
create table paper
(
    id       int auto_increment
        primary key,
    title    tinytext not null,
    url      tinytext not null,
    Category tinytext not null
)
    comment 'paper에 관한 table';

create table tag
(
    id  int auto_increment
        primary key,
    tag tinytext not null
)
    comment 'tag';

create table fast_paper
(
    id       int auto_increment
        primary key,
    paper_id int not null,
    tag_id   int null,
    constraint paper_id_fk
        foreign key (paper_id) references paper (id),
    constraint tag_id_fk
        foreign key (tag_id) references tag (id)
)
    comment '작성한 글';
```
