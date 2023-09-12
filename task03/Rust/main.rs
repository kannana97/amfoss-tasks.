use std::io;

fn is_prime(num: u32) -> bool {
    if num <= 1 {
        return false;
    }
    if num == 2 {
        return true;
    }
    if num % 2 == 0 {
        return false;
    }
    let sqrt_num = (num as f64).sqrt() as u32;
    for i in (3..=sqrt_num).step_by(2) {
        if num % i == 0 {
            return false;
        }
    }
    true
}

fn main() {
    let mut input = String::new();
    println!("Enter a number: ");
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read input");
    let n: u32 = input.trim().parse().expect("Invalid input");

    println!("Prime numbers up to {} are:", n);
    for i in 2..=n {
        if is_prime(i) {
            print!("{} ", i);
        }
    }
    println!();
}

