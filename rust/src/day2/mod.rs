
// pub fn part_2() {
//     let input: Vec<&str> = include_str!("input.txt").split_whitespace().collect();;
//     let (a, b) = part_2_run(&input);
//     print_result(a, b);
// }

pub fn part_2_run<'a>(input: &'a Vec<&str>) -> (&'a str, &'a str) {  
    for i in 0..input.len() {
        for j in i+i..input.len() {
            if has_one_different(input[i],input[j]) {
                return (input[i],input[j]);
            }
        }        
    }
    unreachable!()
}

pub fn part_2_run_alt<'a>(input: &'a Vec<&str>)-> String {  
    for i in 0..input.len() {
        for j in i+i..input.len() {
            if has_one_different(input[i],input[j]) {
                return merge(input[i],input[j]);
            }
        }    
    }
    
    unreachable!();
}

fn merge(a: &str, b:&str) -> String {
    a.chars().zip(b.chars()).filter(|(i,j)| i == j)
        .map(|(i,_)| i).collect()    
}

fn has_one_different(a: &str, b: &str) -> bool {
    let a = a.as_bytes();
    let b = b.as_bytes();
    let mut found_one = false;
    for i in 0..a.len() {
        match (a[i] != b[i], found_one) {
            (true, true) => return false,
            (true, false) => found_one = true,
            (false, _) => continue,
        }
    }
    return found_one
}

fn print_result(a: &str, b: &str) {
    let a = a.as_bytes();
    let b = b.as_bytes();
    for (i,_) in a.iter().zip(b.iter()).filter(|(i,j)| i == j) {
        print!("{}", i)
    }
    println!()
}
