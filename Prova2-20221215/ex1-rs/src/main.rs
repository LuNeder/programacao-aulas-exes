
// preciso lembrar como usa rust pqp viu
use std::io;
use std::str::FromStr;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("cu");
    let mn = input.split(" ");
    let mnv = mn.collect::<Vec<&str>>();
    let m = i32::from_str(mnv[0]).unwrap_or(0);
    let n = i32::from_str(mnv[1]).unwrap_or(0);

    ackermann(m, n);
}

fn ackermann(m: i32, n: i32) {
    if m == 0 {
        println!("m {} n {}", m, n)
    }

}