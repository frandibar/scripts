with import <nixpkgs> {};

((python310.withPackages (ps: with ps; [
  beautifulsoup4
]))
).env
