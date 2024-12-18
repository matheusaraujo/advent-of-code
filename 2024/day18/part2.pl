# TODO: @matheusaraujo - brute force, this code needs to be refactored

use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;

    for my $i ( 1024 .. $#puzzle_input ) {
        my $answer    = q{};
        my $count     = 0;
        my %corrupted = ();
        for my $line (@puzzle_input) {
            my ( $x, $y ) = split /,/smx, $line;
            $corrupted{"$x,$y"} = 1;
            $count++;
            if ( $count == $i ) {
                $answer = "$x,$y";
                last;
            }
        }

        if ( dfs( 71, \%corrupted ) == -1 ) {
            return $answer;
        }
    }
    return '-1,-1';
}

# sub dfs {

#     my ( $size, $corrupted ) = @_;
#     my @directions = ( [ 0, 1 ], [ 1, 0 ], [ 0, -1 ], [ -1, 0 ] );
#     my @queue      = ( [ 0, 0, 0 ] );
#     my %visited    = ();

#     while (@queue) {

#         my $current = shift @queue;
#         my ( $x, $y, $steps ) = @{$current};

#         $visited{"$x,$y"} = 1;

#         if ( $x == $size - 1 && $y == $size - 1 ) {
#             return $steps;
#         }

#         for my $direction (@directions) {
#             my ( $dx, $dy ) = @{$direction};

#             my $nx = $x + $dx;
#             my $ny = $y + $dy;

#             if (   $nx < 0
#                 || $nx >= $size
#                 || $ny < 0
#                 || $ny >= $size
#                 || exists $visited{"$nx,$ny"}
#                 || exists $corrupted->{"$nx,$ny"} )
#             {
#                 next;
#             }

#             $visited{"$nx,$ny"} = 1;

#             push @queue, [ $nx, $ny, $steps + 1 ];
#         }
#     }

#     return -1;
# }

1;
