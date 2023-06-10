mod quick;

use quick::quicksort;

fn main() {
    let mut t: Vec<usize> = vec![
        5, 7, 6, 321, 68, 6, 1, 7, 3, 9, 7, 20, 3, 94846, 16, 84, 6, 3486,
    ];
    quicksort(&t);
    assert_eq!(
        t,
        vec![1, 3, 3, 5, 6, 6, 6, 7, 7, 7, 9, 16, 20, 68, 84, 321, 3486, 94846]
    );
}
