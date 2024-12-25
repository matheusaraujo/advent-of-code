use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my $result       = 0;
    my ( $locks, $keys ) = parse_input(@puzzle_input);

    for my $key ( @{$keys} ) {
        for my $lock ( @{$locks} ) {
            my $overlap = any_overlap( $lock, $key );
            $result += $overlap ? 0 : 1;
        }
    }

    return $result;
}

sub any_overlap {
    my ( $lock, $key ) = @_;
    for my $i ( 0 .. 4 ) {
        return 1 if $lock->[$i] + $key->[$i] >= 6;
    }
    return 0;
}

sub parse_input {
    my @puzzle_input = @_;
    my @keys         = ();
    my @locks        = ();
    my $i            = 0;

    while ( $i < scalar @puzzle_input ) {
        my $line = $puzzle_input[$i];

        if ( $line eq '#####' ) {
            push @locks, parse_lock( \@puzzle_input, \$i );
        }
        elsif ( $line eq '.....' ) {
            push @keys, parse_key( \@puzzle_input, \$i );
        }
        $i++;
    }

    return ( \@locks, \@keys );
}

sub parse_lock {
    my ( $input_ref, $index_ref ) = @_;
    my @lock = ( 0, 0, 0, 0, 0 );

    for ( 1 .. 6 ) {
        ${$index_ref}++;
        my @chars = split //sxm, $input_ref->[ ${$index_ref} ];
        for my $k ( 0 .. 4 ) {
            $lock[$k] += $chars[$k] eq q{#} ? 1 : 0;
        }
    }

    return \@lock;
}

sub parse_key {
    my ( $input_ref, $index_ref ) = @_;
    my @key = ( 5, 5, 5, 5, 5 );

    for ( 1 .. 6 ) {
        ${$index_ref}++;
        my @chars = split //sxm, $input_ref->[ ${$index_ref} ];
        for my $k ( 0 .. 4 ) {
            $key[$k] -= $chars[$k] eq q{.} ? 1 : 0;
        }
    }

    return \@key;
}

1;
