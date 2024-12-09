#!/usr/bin/perl
use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;
    my $result       = 0;
    chomp @puzzle_input;

    my ( $is_file, $file_id, $left_pointer, $right_pointer, $file_size,
        $free_size )
      = ( 1, 0, 0, 0, 0, 0 );
    my @memory = ();

    foreach my $char ( split //sm, $puzzle_input[0] ) {
        my $id = $is_file ? $file_id : q{.};
        for ( 1 .. $char ) {
            $memory[ $left_pointer++ ] = $id;
        }
        $file_id += $is_file ? 1 : 0;
        $is_file = !$is_file;
    }

    $right_pointer = $#memory;
    $file_id       = $file_id - 1;

    while ( $file_id >= 0 ) {

        while ( $right_pointer > -1 && $memory[$right_pointer] ne $file_id ) {
            $right_pointer--;
        }

        $file_size = 0;
        while ( $right_pointer > -1 && $memory[$right_pointer] eq $file_id ) {
            $right_pointer--;
            $file_size++;
        }

        $left_pointer = 0;
        while ( $left_pointer < $right_pointer ) {

            while ($left_pointer < $right_pointer
                && $memory[$left_pointer] ne q{.} )
            {
                $left_pointer++;
            }

            $free_size = 0;
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

    for my $i ( 0 .. $#memory ) {
        $result += $memory[$i] eq q{.} ? 0 : $i * $memory[$i];
    }

    return $result;

}

1;

