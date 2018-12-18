use criterion::{criterion_group, criterion_main, Criterion};

extern crate adventofcode2018;
use adventofcode2018::day2::*;
use adventofcode2018::day3;



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

fn day3_part1(c: &mut Criterion) {
    c.bench_function("day 3 part 1", move |b| {
        b.iter(|| day3::part1())
    });
}

fn day3_part2(c: &mut Criterion) {
    c.bench_function("day 3 part 2", move |b| {
        b.iter(|| day3::part2())
    });
}

fn day3_part2_overlap_set(c: &mut Criterion) {
    c.bench_function("day 3 part 2 overlap set", move |b| {
        b.iter(|| day3::part2_overlap_set())
    });
}

// criterion_group!(benches,
//                  part_2_mine,
//                  part_2_mine_merge,
// );

criterion_group!(day3,
                 day3_part1,
                 day3_part2,
                 day3_part2_overlap_set);
criterion_main!(day3);
