use criterion::{criterion_group, criterion_main, Criterion};

extern crate adventofcode2018;
use adventofcode2018::day2::*;



fn part_2_mine(c: &mut Criterion) {
    c.bench_function("mine", move |b| {
        b.iter_with_setup(move || include_str!("../src/day2/input.txt").split_whitespace().collect(),
                          |input| { part_2_run(&input); })
    });
}

fn part_2_mine_merge(c: &mut Criterion) {
    c.bench_function("mine merge", move |b| {
        b.iter_with_setup(move || include_str!("../src/day2/input.txt").split_whitespace().collect(),        
                          |input| { part_2_run_alt(&input); } )
    });
}

criterion_group!(benches,
                 part_2_mine,
                 part_2_mine_merge,
);
criterion_main!(benches);
