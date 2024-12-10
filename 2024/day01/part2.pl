use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;
    my $result       = 0;
    my %count        = ();

    my ( $list1_ref, $list2_ref ) = parse_input(@puzzle_input);
    my @list1 = @{$list1_ref};
    my @list2 = @{$list2_ref};

    foreach my $n2 (@list2) {
        $count{$n2}++;
    }

    foreach my $n1 (@list1) {
        if ( exists $count{$n1} ) {
            $result += $n1 * $count{$n1};
        }
    }

    return $result;
}

1;

