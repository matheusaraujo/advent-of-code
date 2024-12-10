use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my $result       = 0;

    my ( $list1_ref, $list2_ref ) = parse_input(@puzzle_input);
    my @list1 = @{$list1_ref};
    my @list2 = @{$list2_ref};

    foreach my $i ( 0 .. $#list1 ) {
        $result += abs $list1[$i] - $list2[$i];
    }

    return $result;
}

1;
