use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;

    my ( $undef,        @memory )        = map_input_to_memory(@puzzle_input);
    my ( $left_pointer, $right_pointer ) = ( 0, $#memory );

    while ( $left_pointer <= $right_pointer ) {
        while ( $memory[$right_pointer] eq q{.} ) {
            $right_pointer--;
        }

        if ( $memory[$left_pointer] eq q{.} ) {
            $memory[$left_pointer]  = $memory[$right_pointer];
            $memory[$right_pointer] = q{.};
            $left_pointer++;
            $right_pointer--;
        }
        else {
            $left_pointer++;
        }
    }

    return calculate_checksum(@memory);
}

1;
