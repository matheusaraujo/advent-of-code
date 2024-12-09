#!/usr/bin/perl
use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my $result       = 0;
    chomp @puzzle_input;

    my ( $is_file, $file_id, $left_pointer, $right_pointer ) = ( 1, 0, 0, -1 );
    my @memory = ();

    foreach my $char ( split //sm, $puzzle_input[0] ) {
        my $id = $is_file ? $file_id : q{.};
        for ( 1 .. $char ) {
            $memory[ $left_pointer++ ] = $id;
        }
        $file_id += $is_file ? 1 : 0;
        $is_file = !$is_file;
    }

    $left_pointer  = 0;
    $right_pointer = $#memory;

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

    for my $i ( 0 .. $#memory ) {
        $result += $memory[$i] eq q{.} ? 0 : $i * $memory[$i];
    }

    return $result;
}

1;
