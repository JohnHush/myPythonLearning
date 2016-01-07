import pylab, random, string, copy

class Point( objects ):
    '''
    Represents the original Data
    '''
    def __init__( self , name , originalAttrs , normalizedAttrs = None ):
        self.name = name
        self.unNormalized = originalAttrs
        if normalizedAttrs == None:
            self.attrs = orriginalAttrs
        else:
            self.attrs = normalizedAttrs

    def dimensionality( self ):
        return len( self.attrs )
    def getAttrs( self ):
        return self.attrs
    def getOriginalAttrs( self ):
        return self.unNormalized
    def distance( self , other ):
        #Euclidean distance metric
        result = 0.
        for i in range( self.dimensionality() ):
            result += ( self.attrs[i] - other.attrs[i] )**2
        return result**0.5
    def getName( self ):
        return self.name
    def toStr( self ):
        return self.name + str( self.attrs )
    def __str__( self ):
        return self.name

class Cluster( object ):
    def __init__( self , points , pointType ):
        self.points = points
        self.pointType = pointType
        self.centroid = self.computeCentroid()

    def singleLinkageDist( self, other ):
        minDist = self.points[0].distance(other.points[0])
        for p1 in self.points:
            for p2 in other.points:
                if p1.distance(p2) < minDist:
                    minDist = p1.distance( p2 )
        return minDist
    def maxLinkageDist( self , other ):
        maxDist = self.points[0].distance( other.points[0] )
        for p1 in self.points:
            for p2 in other.points:
                if p1.distance(p2) > maxDist:
                    maxDist = p1.distance(p2)
        return maxDist
    def averageLinkageDist( self, other ):
        totDist = 0.0
        for p1 in self.points:
            for p2 in other.points:
                totDist += p1.distance( p2 )
        return totDist/( len(self.points)*len(other.points) )
    def update( self , points ):
        oldCentroid = self.centroid
        self.points = points
        if len( points )>0:
            self.centroid = self.computeCentroid()
            return oldCentroid.distance( self.centroid )
        else:
            return 0.
    def members( self ):
        for p in self.points:
            yield p
    def isIn( self , name ):
        for p in self.points:
            if p.getName() == name:
                return True
        return False
    def toStr( self ):
        result = ''
        for p in self.points:
            result = result + p.toStr() + ','
        return result[:-2]
    def __str__( self ):
        names = []
        for p in self.points:
            names.append( p.getName() )
        names.sort()
        result = ''
        for p in names:
            result = result + p + ','
        return result[:-2]
    def getCentroid( self ):
        return self.centroid
    def computeCentroid( self ):
        dim = self.points[0].dimensionality()
        totVals = pylab.array( [0.0]*dim )
        for p in self.points:
            totVals += p.getAttrs()
        centroid = self.pointType( 'mean',
                                    totVals/float(len(self.points)),
                                    totVals/float(len(self.points)))
        return centroid
class ClusterSet( object ):
    def __init__( self , pointType ):
        self.members = []
    def add( self , c ):
        if c in self.members:
            raise ValueError
        self.members.append(c)
    def getClusters( self ):
        return self.members[:]
    def mergeClusters( self , c1 , c2 ):
        points = []
        for p in c1.members():
            points.append(p)
        for p in c2.members():
            points.append(p)
        newC = Cluster( points , type(p) )
        self.members.remove(c1)
        self.members.remove(c2)
        self.add(newC)
        return c1, c2
    def findClosest( self , metric ):
        minDistance = metric( self.members[0] , self.members[1] )
        toMerge = ( self.members[0] , self.members[1] )
        for c1 in self.members:
            if c1== c2:
                continue
            if metric( c1, c2 ) < minDistance:
                minDistance = metric ( c1 , c2 )
                toMerge = ( c1 , c2 )
        return toMerge
    def mergeOne( self , metric , toPrint = False ):
        if len( self.members ) ==1:
            return None
        if len( self.members ) ==2:
            return self.mergeClusters( self.members[0] , self.members[1] )
        toMerge = self.findClosest( metric )
        if toPrint:
            print 'Merged'
            print '   '+ str( toMerge[0] )
            print 'with'
            print '   '+ str( toMerge[1] )
        self.mergeClusters( toMerge[0] , toMerge[1] )
        return toMerge
    def mergeN( self , metric , numClusters =1 , history = [] , toPrint = False ):
        assert numClusters >= 1
        while len( self.members ) > numClusters:
            merged = self.mergeOne( metric , toPrint )
            history.append( merged )
        return history
    def numClusters( self ):
        return len( self.members ) +1 
    def __str__( self ):
        result = ''
        for c in self.members:
            result = result + str(c) + '\n'
        return result

