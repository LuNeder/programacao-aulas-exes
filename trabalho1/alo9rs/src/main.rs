use std::io;

fn main() {
   let mut number = String::new();
   io::stdin()
        .read_line(&mut number)
        .expect("Failed to read input");

    let ord = ["primeiro", "segundo", "terceiro", "quarto"];
    let mut indice = 0;
    
    for i in number.replace("\n", "").chars() {
        println!("O {} dígito é {}", ord[indice], i);
        indice += 1;
    }
    
    
}
