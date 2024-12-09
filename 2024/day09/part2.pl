use strict;
use warnings;

sub part2() {
    my @puzzle_input = @_;

    my ( $file_id,      @memory )        = map_input_to_memory(@puzzle_input);
    my ( $left_pointer, $right_pointer ) = ( 0, $#memory );

    while ( $file_id >= 0 ) {
        while ( $memory[$right_pointer] ne $file_id ) {
            $right_pointer--;
        }

        my $file_size = 0;
        while ( $memory[$right_pointer] eq $file_id ) {
            $right_pointer--;
            $file_size++;
        }

        $left_pointer = 0;
        while ( $left_pointer < $right_pointer ) {
            while ( $memory[$left_pointer] ne q{.} ) {
                $left_pointer++;
            }

            if ( $left_pointer >= $right_pointer ) {
                last;
            }

            my $free_size = 0;
            while ( $memory[$left_pointer] eq q{.} ) {
                $left_pointer++;
                $free_size++;
            }

            if ( $file_size <= $free_size ) {
                for my $i ( 0 .. $file_size - 1 ) {
                    $memory[ $left_pointer - $free_size + $i ] = $file_id;
                    $memory[ $right_pointer + $i + 1 ] = q{.};
                }
                last;
            }
        }

        $file_id--;
    }
    return calculate_checksum(@memory);
}

1;

