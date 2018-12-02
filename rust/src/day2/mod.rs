pub fn part_2() {
    let input: Vec<&str> = include_str!("input.txt").split_whitespace().collect();    
    for i in 0..input.len() {
        for j in i+i..input.len() {
            if has_one_different(input[i],input[j]) {
                print_result(input[i],input[j]);
                return;
            }
        }        
    }
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
    for (i,_) in a.chars().zip(b.chars()).filter(|(i,j)| i == j) {
        print!("{}", i)
    }
    println!()
}

    
