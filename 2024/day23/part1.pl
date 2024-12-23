use strict;
use warnings;
use List::Util qw(any);

sub part1 {
    my @puzzle_input    = @_;
    my %graph           = ();
    my %triangles       = ();
    my @valid_triangles = ();

    for my $line (@puzzle_input) {
        my ( $a, $b ) = split /-/sxm, $line;
        push @{ $graph{$a} }, $b;
        push @{ $graph{$b} }, $a;
    }

    foreach my $node ( keys %graph ) {
        my @neighbors = @{ $graph{$node} };
        for my $i ( 0 .. $#neighbors - 1 ) {
            for my $j ( $i + 1 .. $#neighbors ) {
                my $n1 = $neighbors[$i];
                my $n2 = $neighbors[$j];
                if ( any { $_ eq $n2 } @{ $graph{$n1} } ) {
                    my @triangle = sort $node, $n1, $n2;
                    $triangles{ join q{,}, @triangle } = 1;
                }
            }
        }
    }

    @valid_triangles = grep {
        my @nodes = split /,/sxm;
        grep { /^t/sxm } @nodes;
    } keys %triangles;

    return scalar @valid_triangles;
}

1;
