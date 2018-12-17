use std::collections::HashSet;

pub fn solve_part_2() {
    let input = include_str!("../../../inputs/day1.txt");
    
    let mut found = HashSet::new();
    found.insert(0);
    let result = input.split_whitespace()
        .map(|x| x.parse::<isize>().unwrap())
        .cycle()
        .scan(0, |sum, c| {
            *sum += c;
            Some(sum.clone())
        }).find_map(|sum| found.replace(sum));
    println!("{}", result.unwrap())
}
