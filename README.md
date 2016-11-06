# RAreducts
Generates the signatures that are reducts of the signature of Tarski's relation algebras along with domain and range operators. 487 unique signatures are generated, 239 of which include composition. Without domain and range operators there are 200 unique signatures, 100 of which include composition.

The Tarski relation algebra signature consists of:
  - composition
  - lattice operations (join and meet)
  - converse
  - complementation
  - constants 0, 1' and 1, where 0 is intended to be represented as the empty relation, 1' as the identity relation, and 1 as the largest equivalence relation. 0 and 1 are bottom and top elements of the lattice.
  
For more information about relation algebras, see [2], or Tarski's original paper [3].

This is a collection of methods used to generate the list of reduct signatures. In particular, generateSignatures(["comp"]) is called on to generate the list of reducts of the full signature capable of expressing at least composition. The order in which these operations are displayed in each signature is maintained through the sigSort method.
  
The full signature used here is the Tarski signature along with the partial order derived from the lattice operations, as well as domain and range operators $\dom$ and $\ran$. Thus, the full signature considered is
    comp, join, meet, le, con, -, id, 0, top, dom, ran
    
A signature may be capable of expressing operations not explicitly listed. For example, any signature containing a lattice operation a lattice operation is equipped with a partial order inherited from that operation. In order to avoid redundancy in the full list, each signature is 'completed' according to the rules expressed in [1].
 
# References 
[1] R. Hirsch. The finite representation property for reducts of relation algebra,
2011. Manuscript. http://www.cs.ucl.ac.uk/fileadmin/UCL-CS/staff/Robin_Hirsch/Papers/domain_fin.pdf.
  
[2] R. D. Maddux. Relation Algebras, volume 150 of Studies in Logic and the
Foundations of Mathematics. Elsevier B. V., Amsterdam, 2006.

[3] A. Tarski. On the calculus of relations. J. Symbolic Logic, 6:73–89, 1941. xvii.

