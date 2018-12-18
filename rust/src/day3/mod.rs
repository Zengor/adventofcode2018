use lazy_static::lazy_static;
use regex::Regex;
use hashbrown::{HashMap, HashSet};
use itertools::Itertools;

use std::str::FromStr;

pub struct Rect {
    id: u16,
    left: u16,
    top: u16,
    right: u16,
    bottom: u16,
}

impl Rect {
    fn new(id: u16, x: u16, y: u16, w: u16, h: u16) -> Self {
        Self {
            id,
            left: x,
            top: y,
            right: x + w,
            bottom: y + h,
        }
    }
}

impl FromStr for Rect {
    type Err = std::num::ParseIntError;

    fn from_str(claim: &str) -> Result<Self, Self::Err> {
        lazy_static! {            
            static ref RE: Regex = Regex::new(r"(?x)
                \#
                (?P<id>[0-9]+)
                \s+@\s+
                (?P<x>[0-9]+),(?P<y>[0-9]+):
                \s+
                (?P<w>[0-9]+)x(?P<h>[0-9]+)
            ").unwrap();
        }
        let matches = RE.captures(claim).expect("failed capture");
        Ok(Rect::new(
            matches["id"].parse()?,
            matches["x"].parse()?,
            matches["y"].parse()?,
            matches["w"].parse()?,
            matches["h"].parse()?,
        ))
    }
}

pub fn populate_grid(claims: &Vec<Rect>) -> HashMap<(u16,u16),u16> {
    let mut grid: HashMap<(u16,u16),u16> = HashMap::new();
    for claim in claims {
        for point in (claim.left..claim.right).cartesian_product(claim.top..claim.bottom) {
            *grid.entry(point).or_default() += 1
        }
    }
    grid
}

pub fn part1() {
    let input = include_str!("../../../inputs/day3.txt");
    let claims = input.lines().map(|l| l.parse().expect("failed_parsing")).collect();
    let grid = populate_grid(&claims);
    let count = grid.values().filter(|&&count| count > 1).count();
    //println!("{}", count);
}

pub fn part2() {
    let input = include_str!("../../../inputs/day3.txt");
    let claims = input.lines().map(|l| l.parse().expect("failed_parsing")).collect();
    let grid = populate_grid(&claims);
    for claim in claims {
        let mut claim_points = (claim.left..claim.right).cartesian_product(claim.top..claim.bottom);
        if claim_points.all(|x| grid[&x] == 1) {
            //println!("no overlap: {}", claim.id);
            return;
        }
    }
}

fn detect_collision(a: &Rect, b: &Rect) -> bool {
    (a.left < b.right &&
        a.right > b.left &&
        a.top < b.bottom &&
        a.bottom > b.top)
}


// adds ids of all claims that overlap into a set and then runs over the structure again
// to find one that doesn't. added to compare benchmarks
pub fn part2_overlap_set() {
    let input = include_str!("../../../inputs/day3.txt");
    let claims: Vec<Rect> = input.lines().map(|l| l.parse().expect("failed_parsing")).collect();
    // a set of all rects
    let mut overlap: HashSet<u16> = HashSet::with_capacity(claims.len());
    for (i, claim_i) in claims.iter().enumerate() {
        for claim_j in claims[i+1..].iter() {
            if detect_collision(claim_i,claim_j) {
                overlap.insert(claim_i.id);
                overlap.insert(claim_j.id);
            }
        }
    }
    for id in claims.iter().map(|c| c.id) {
        if !overlap.contains(&id) {
            //println!("no overlap: {}", id);
            return;
        }
    }
}
