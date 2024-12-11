use strict;
use warnings;

sub parse_input {
    my @lines = @_;
    return map { [ split //sm ] } @lines;
}

1;
