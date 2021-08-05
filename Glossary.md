---
title: Glossary
tags: glossary
---

Glossary
===

# **[A](#A)  [B](#B)  [C](#C)  [D](#D)  [E](#E)  [F](#F)  [G](#G)  [H](#H)  [I](#I)  [J](#J)  [K](#K)  [L](#L)  [M](#M)  [N](#N)  [O](#O)  [P](#P)  [Q](#Q)  [R](#R)  [S](#S)  [T](#T)  [U](#U)  [V](#V)  [W](#W)  [X](#X)  [Y](#Y)  [Z](#Z)**


---

[<i class="fa fa-arrow-circle-right"></i> German Version](https://hackmd.io/@materialdigital/SyUidXuRu)

# A

## A-Box
[ id=a-box ]
In an [ontology](#ontology), the A-box represents the state of the modeled world. It contains the [individuals / instances](#instance) of a domain in the form of facts, their [properties](#property), and the relations to each other. For this purpose, it makes use of the [T-Box](#T-Box)

## Academic Projects
[ id=academic_projects ]
Projects and resulting consortia from the 1st supplementary [BMBF](#BMBF) call MaterialDigital under the MaterialDigital innovation platform. Primarily in collaboration with the Innovation Platform, they are to develop content and building blocks for PMD based on [Use Cases](#Use-Cases)

## Accessibility
[ id=accessible ]
This term is part of the [FAIR](#FAIR) principle.

## Agile Management
[ id=agile_management ]
Agile management provides a methodology to act flexibly, pro-actively, anticipatively and proactively to introduce necessary changes. Typical elements of agile management are roles, [sprints](#sprint), and [user stories](#user story).

## Agile Manager (AM)
[ id=agile_manager ]
A role in [agile management](#agile_management). The agile manager assists the team in an [agile management](#agiles management) with communication, organizes meetings, ensures adherence to roles and form, keeps track of the team, communicates issues to the [product owner](#product owner), prepares the agenda, and ensures proper documentation of the team.

## application ontology
[ id=application_ontology ]
A (partial)[ontology](#ontology) that contains, structures, and describes, specific [entities](#entities) for a defined [use case/use cases](#use cases). It can be assumed that at least one application ontology has to be created per use case of the PMD and thus per funded project, depending on the use/goal of the ontology itself, in order to integrate the generated information in a retrievable way.

## API
[ id=api ]
An Automatic Programming Interface. An API is an endpoint from one IT system into another. To do this, the API "listens" for requests that are in such a data structure that it understands. Internal programming can then develop a response to this request, which the API spits back out to the very same unified data structure. APIs thus enable the connecting interfaces between systems. Examples include database queries such as SQL or [SPAQRL](#SPARQL).

---


# B

## Backlog
[ id=backlog ]
In an [agile framework](#agile-management), a backlog contains project-related subtasks that need to be completed. They result from breaking down [user stories](#user-story) into individually executable technical actions to be implemented by a team member.

## Blazegraph
[ id=blazegraph ]
A [triplestore](#triplestore), or graph database. It provides an interface to upload ontologies and data, and provides a SPARQL endopoint.

## BLOB
[ id=blob ]
Serialized data, which can thereby be stored like a long text and deserialized if necessary, but whose single values cannot be queried directly.


## BMBF
[ id=bmbf ]
BMBF is the abbreviation for "Bundesministerium für Forschung und Bildung" (Federal Ministry for Research and Education) and supports research in all fields of science by financial means.



---

# C

## Central PMD instance (PMD-C)
[ id=central_pmd_instance ]
PMD [instance](#instance) established at KIT on which the [workflow environments](#workflow environment) run permanently and on which all tools can be installed and tested. 

## Class
[ id=class ]
~~s. "[concept](#concept)"~~ 
A [class](#class) provides an abstraction mechanism for grouping resources with similar characteristics. Every class is associated with a set of individuals, called the class extension. The individuals in the class extension are called the instances of the class. A class has an intensional meaning i.e., the underlying concept.

## CLI
[ id=cli ]
Command Line Interface. Control of computers via specialized commands entered by keyboard into a mask.

## command line
[ id=command_line]
s. [CLI](#CLI)

## Community
[ id=community ]
By community, PMD means all interested parties in the scientific and industrial community.

## concept
[ id=concept ]
A shared conceptualization for an entity uniformly regarded as a closed thing. Examples include "process", "material", "peace", "happiness". They can be used to express the intensional meaning of classes based on their use within the target domain.
~~Together with [Properties](#Property), [T-Box](#T-Box) in [Triple](#Triple--Triple) allows to make statements about the relations of concepts. Concepts then correspond to the subject and object of the triple. Concepts are to be used synonymously with "[classes](#class)" and "objects".~~

## Core Ontology
[ id=core_ontology ]
The Core Ontology shall define unified concepts for the PMD, to which the [Application Ontologies](#Application Ontology) can in turn refer across domains. This shall enable domain-independent standardization in information structuring. An example would be that the [class](#class) "Process" would be present in the Core Ontology, since it is cross-cutting, and the class "fatigue test" would refer to Process as a subclass in an application ontology.

## curation
[ id=curation ]
Curation or curation process in PMD describes the ongoing adaptation and review of [software tools](#software tool), [ontologies](#ontology), and workflows for quality assurance.

---

# D

## data_type
[ id=data_type ]
A data type schematically describes a data structure. It can be used for identification as well as for structural description of resources. A storage in a datatype registry ensures a machine readability of the datatypes.

## Datatype Property
[ id=data_property ]
Specialized [Property](#Property). Datatype properties link individuals to data values. A datatype property is defined as an instance of the built-in OWL class owl:DatatypeProperty. ~~Corresponds in the sense of [RDF](#RDF) to the verb of [triple](#Triple--Triple).~~

## Definition of Done
[ id=definition_of_done ]
Definition in an [agile framework](#agile management) of when a [user story](#user story) is complete. The Definition of Done (DoD) defines the functionality from the user's perspective that is required to fulfill that user requirement.

## Docker Container
[ id=docker_container ]
A Docker Container is a standard software entity that packages the code and all of its dependencies so that the application can be executed quickly and reliably from one computing environment to another.

## domain experts / community
[ id=domain_experts/community ]
Scientific experts who (further) develop their domain within PMD in the context of [use cases](#use cases). The scientific community as a whole thereby shapes the PMD both through their contribution and through participation methods. The selection of the scientific sub-fields represented in the PMD is based on the contributions of the domain experts.





---

# E

## Epic
[ id=epic]
Overarching theme, comparable to [milestones](#milestone). Epics consist of numerous [user stories](#user story) and clearly stated tasks. They represent a "minimum viable or viable [product](#product)."

---

# F


## FAIR
[ id=fair ]
According to Wilkinson et al. (2016), data should be [Findable](#Findable), [Accessible](#Accessible), [Interoperable](#Interoperable), and [Reusable](#Reusable). The acronym has recently become popular to summarize the overarching unified data organization goals of science. For more info please refer to: 
Mark D Wilkinson, Michel Dumontier, IJsbrand Jan Aalbersberg, et al. 2016. [The FAIR Guiding Principles for scientific data management and stewardship](https://www.nature.com/articles/sdata201618). Scientific data 3, 1 (2016), 1–9.

## Findable 
[ id=findable ]
Data that is considered "Findable" should be easily discoverable by both humans and computer systems. This term is part of the [FAIR](#FAIR) principle.

## framework
[ id=framework ]
A framework is a framework structure which is necessary to populate the data space.


---

# G

## GitLab / GitHub
[ id=gitlab/github ]
Gitlab is a web-based application where you can collaborate in projects. Projects are archived in repositories and [versioning](#versioning) is possible. GitHub is very similar to Gitlab, but publicly available to everyone. Usually GitLab is used for project management and GitHub for publishing results.

## Governance
[ id=governance ]
The governance forms the common steering structure for involved projects and collaboration partners in the context of building the [Platform MaterialDigital](#Platform-MaterialDigital). It can be downloaded from the download area of the website.

## GUI
[ id=gui ]
GUI stands for graphical user interface and describes a user interface of a computer with the 
input (e.g. mouse or gestures). By means of graphic symbols and control elements it makes application software operable. The GUI replaces thereby program control by the [command line](#command line) and makes software intuitively and for laymen operable.

---

# H

## HackMD
[ id=hackmd]
Ability to work collaboratively on text. HackMD supports MarkDown.

---

# I

## Industrial projects
[ id=industrial_projects ]
Projects and resulting consortia from the 2nd supplementary [BMBF](#BMBF) call MaterialDigital in the context of the Innovation Platform MaterialDigital. They are primarily to develop content and building blocks for PMD in collaboration with the Innovation Platform.

## Inference / Inference
[ id=inference ]
The inference derived from [Reasoning](#reasoning).

## Instance
[ id=instance ]
Individual realization of a [concept](#concept). For example, the concept tensile test may be instantiated with a particular tensile test that occurred at a particular time at a particular location and with particular parameters. All instantiations together represent the [ontology](#ontology) [A-Box](#A-Box), where statements are made about instances using the terminology defined in the [T-Box](#T-Box).

## interoperability
[ id=interoperability ]
Interoperability describes data that exists in such a way that it can be exchanged, interpreted, and combined semi-automatically with other data sets. This term is part of the [FAIR](#FAIR) principle.

---

# J

## JSON
[ id=json ]
Java Script Object Notation, A standard object description syntax implemented in JavaScript that can be used to represent [BLOBs](#BLOB).

## Jupyter
[ id=jupyter]
Jupyter is a project to develop open-source software, open-standards and to develop services for interactive computing in different programming languages.

## Jupyter Notebooks
[ id=jupyter_notebooks ]
The Jupyter Notebook is an open-source web application that can be used to create and share documents containing live code, equations, visualizations, and narrative text. It is primarily used for traceable documentation of data evaluations.


---

# K

## knowledge graph
[ id=knowledge_graph ]
A knowledge graph is a kownledge base in form of a graph which describes entities and their relationships structured and instantiated accordingly to [ontologies](#ontology). Knowledge graphs can be used to aggregate large amounts of data and derive collected knowledge.

---

# L

## Linked Data
[ id=linked_data ]
Ability to show relations between directly related or synonymous semantic concepts. Linked Data thus enables searching and linking of complex data structures.

## Literal
[ id=literal ]
A string, float or date that is assigned to a concept by [Datatype Property](#Property). Example: a single value without further information. A literal is given a meaning within the [A-Box](#A-Box).

---

# M

## management_board
[ id=management_board ]
The platform is associated with an industrially staffed management circle convened by the [BMBF](#BMBF). Its purpose is to ensure that project activities are focused on maximum industrial benefit and to ensure optimal transfer of results into application. The management circle meets once or twice a year together with the members of the platform and is involved in the workshops of the project. 

## Mapping
[ id=mapping ]
Mapping involves mapping file elements from different data models to each other.

## Metadata
[ id=metadata ]
Metadata is structured data that contains information about characteristics of other data. 

## milestone
[ id=milestone ]
Milestones circumscribe the overall goals in the project plan. 

## MSE
[ id=mse ]
MSE is short for Material Science Experts and includes our material science experts.

---

# N

---

# O

## Object
[ id=object]
s. "[concept](#concept)"

## Object Property
[ id=object_property ]
The relationship of an [individual](#individual) to another individual. An object property is defined as an instance of the built-in OWL class owl:ObjectProperty.  ~~Corresponds, in terms of [RDF](#RDF), to the verb of [triple](#triple--triple).~~

## ontology
[ id=ontology ]
An ontology is an explicit, formal specification of a shared conceptualization. The term is borrowed from philosophy, where an Ontology is a systematic account of existence. For AI systems, what ‘exists’ is that which can be represented.
~~Explicit, formal structuring of shared [concepts](#concept) that make up a domain.~~ In this context, an ontology contains content links, either descriptive or formal. It goes beyond mere [taxonomic categorization](#taxonomy) and thus can do more than standardization. Whenever possible, an ontology for materials science and engineering must take into account the cross-scale nature of the discipline. It must in itself provide logical added value beyond a relational description.

## OWL
[ id=owl]
OWL, the Web Ontology language is a specification of the [W3C](#Semantic-Web). It is a markup language for developing and publishing ontologies. Its documentation can be found [here](https://www.w3.org/TR/owl-ref/#Property).
~~web [ontology](#ontology) language. It describes hierarchical [classes](#class), attributes and associations of these classes and their relationship to each other.Attributes and associations are collectively called properties of a class. OWL is thus the standardized [RDF](#RDF) syntax agreed upon for the Web.~~

---

# P

## Pain Point
[ id=pain_point ]
In the [agile framework](#agile management), a pain point is a recurring problem that a [stakeholder group](#stakeholder) encounters in the course of its activities and that a member of that group cannot immediately resolve on its own. This creates a willingness to pay on the part of the member for the solution of the Pain Point.

## Parser / Parsing
[ id=parser-parsing ]
A deserializer for [BLOBS](#BLOB), strings, and other large data sets.

## Platform MaterialDigital
[ id=platform_materialdigital ]
The Platform MaterialDigital (PMD) is the infrastructure necessary for a unified exchange and linking of data, software solutions and [ontologies](#ontology) for dealing with materials. It thus represents the unifying technological basis with which data and software from different application fields can be linked. The platform is created and represented by the [Platform Responsible Consortium](#Platform Responsible Consortium- Platform Tr%C3%A4ger) and the [Funded Scientific Projects](#Academic Projects). 

## platform-responsible-consortium/platform-carrier.
[ id=platform_responsible_consortium ]
The consortium that has been managing the MaterialDigital (PMD) platform since its inception in July 2019, consisting of the Federal Institute for Materials Research and Testing (BAM), the Karlsruhe Institute of Technology (KIT), the Max Planck Institute for Iron Research (MPIE), the Fraunhofer Institute for Mechanics of Materials (IWM), and the Leibniz Institute for Materials-oriented Technologies (IWT).

## PMD-Central / PMD-C
[ id=pmd-central-pmd-c ]
Server set up at KIT on which the [workflow environments](#workflow environment) run permanently and on which all tools can be installed and tested.

## Product
[ id=product ]
A product is something created by a process that provides value to a market by solving a sum of predefined [pain points](#pain point) from customers and [stakeholder groups](#stakeholders). 

## Product Owner
[ id=product_owner ]
The Product Owner (PO) is responsible for the wording and implementation of the [User Stories](#User Story). Writes user stories, represents user interests, defines requirements (not solutions), passes responsibility for feasibility to team, defines [Definition of Done](#Definition-of-Done). 

## project spokesperson
[ id=project_spokesperson ]
Elected representative of a funded consortium of an [academic project](#academic-projects) who represents the consortium to the [PMD Steering Committee](#steering committee).

## project sponsor
[ id=project_sponsor ]
Project sponsors are appointed by the [BMBF](#BMBF) and implement the technical and organizational aspects of the ministry's projects. 
They advise prospective sponsors, applicants and grant recipients and are responsible for the administrative processing and technical support of the projects in all phases.

## Property
[ id=property]
s. [Object Property](#Object-Property) and [Data Property](#Data-Property).

## Pyiron
[ id=pyiron ]
Pyiron is a Python-based integrated [workflow environment](#workflow environment) for computational materials science. It provides all the necessary tools to interactively run complex [simulation protocols](#simulation protocol) that can combine different computer codes and perform millions of separate computations on powerful computer clusters.

---

# Q

---

# R

## R-box
[ id=r-box ]
The set of object properties axioms (transitivity, inclusion, symmetry, reflexivity, irreflexicity, disjunctiveness).

~~Subset of [T-Box](#T-Box) containing the relations or [Properties](#Property) (Relationships).~~

## RDF
[ id=rdf ]
Resource-Description-[Framework](#Framework). A standard model to describe and exchange information in a semantically standardized way on the Web. 

## Reasoning
[ id=reasoning ]
Taken together, the [RDF](#RDF) of a [triplestore](#triplestore) results in transitivities. These are used in reasoning to derive more information than just the originally described information. Reasoning is done by a software, the reasoner, which works on the triplestore.

## reusable
[ id=reusable ]
Reusable data.
This term is part of the [FAIR](#FAIR) principle.

---

# S

## Semantic Web
[ id=semantic_web ]
The W3C-compliant [framework](#Framework) that is intended to provide a unique resource description and corresponding query in a standardized way. The Semantic Web is a "stack" of several underlying sub-technologies for the corresponding task areas.

## SimStack
[ id=simstack ]
The [workflow environment](#workflow environment) SimStack enables the efficient design and customization of complex workflows ("rapid prototyping") with software modules from different vendors via drag-and-drop, exposing only settings relevant for the respective [use case](#use cases). Together with the automated execution of the workflows on mainframes, this minimizes the complexity for the end user and the required expertise. This enables the transfer of complex, multi-scale scientific methods to industry. 

## Simulation log
[ id=simulation_log ]
Realization of a materials science workflow in a computer program.

## Software tool
[ id=software-tool ]
Single program for processing a specific material science task. It converts a well-defined input into a well-defined output. Examples are DFT or FEM codes.

## SPARQL
[ id=sparql ]
SPARQL is synonymous with SPARQL Protocol And RDF Query Language and is a graph-based query language for querying content from the Resource Description [Framework](#Framework) ([RDF](#RDF)), which is used in databases to formulate logical statements about arbitrary things.

## sprint
[ id=sprint ]
In an [agile framework](#agile management), a sprint means a phase of work by a team designed to deliver [user stories](#user story).

## Stakeholder
[ id=stakeholder ]
Stakeholders are people and groups that have an interest in the course, results and processes of a project / [product](#product). It is also important to consider this interest in projects.

## Standardization
[ id=standardization ]
Standardization is the formulation, issuance and application of rules, guidelines or characteristics by a recognized organization and its standards bodies. In the case of the platform, we work together with DIN.

## Steering Committee
[ id=steering_committee ]
The executive plenary of the [platform responsible 
Consortium](#Platform Responsible Consortium--Platform Tr%C3%A4ger), represented by a spokesperson and one additional representative per funded organization.

---


# T

## Taxonomy
[ id=taxonomy ]
A taxonomy is a hirarchical breakdown in a classification system.

## T-box
[ id=t-box ]
The T-Box describes the Terminological Formalism and contains the knowledge about the [classes](#class) of the domain.
The T-Box defines which [classes](#class) of objects exist in the domain and what properties they have.

## token
[ id=token ]
A randomized system key that can be used for authentication, for example. The user usually does not get to see a token.

## Transitivity
[ id=transitivity ]
Logical [inference](#inference) according to the motto if A acts on B and B acts on C, then A acts on C as well. This becomes exploitable in the class hierarchy and other [Object Properties](#Object-Property) in [OWL](#owl) by [Reasoning](#Reasoning).

## triple
[ id=triple ]
A triple is a statement consisting of subject, predicate, and object, such as "man" - "is son of" - "woman". Triples are described uniformly with by [RDF](#RDF). ~~, leading to the [T-Box](#T-Box).~~ ~~They can then be associated with [instances](#instance), leading to the [A-box](#A-box), and allowing statements such as in the example "Karl" - "is son of" - "Anita".~~

## triplestore
[ id=triplestore ]
A triplestore is a database in which [triples](#triple--triples) can be stored and retrieved by semantic queries.
The triple represents one data entity at a time.

## Turtle
[ id=turtle ]
A standardized [RDF](#RDF) serialization.

---

# U

## Use Cases
[ id=use_cases ]
Use cases that are implemented based on the platform, generated as part of funded projects, and structured to be compatible with the platform. 

## User Story
[ id=user_story ]
A user story is the smallest unit from a user's perspective in an [agile framework](#agile management). It defines the desired functionality that the user envisions to solve exactly one of his [pain points](#pain point)

---

# V

## Versioning
[ id=versioning ]
A versioning captures changes to documents or data.

---

# W

## Web Ontology Language (OWL)
[ id=web_ontology_language ]
s.[OWL](#OWL)

## wikibase
[ id=wikibase ]
Open source graph database, knowledge database, queryable via [SPARQL](#SPARQL). However, Wikibase uses a relational data structure inside and is not migratable to other graph solutions without other.

## workflow environment
[ id=workflow_environment ]
Software installed on a PMD server instance within which other [software tools](#software tool) can be executed and combined in [simulation protocols](#simulation protocol). Uniform interfaces are governed by workflow environments.


---

# X


---

# Y


---

# Z
